import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

class BeginnerNN:
    def __init__(self, input_size, output_size, hidden_size, learning_rate):
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_size = hidden_size
        self.learning_rate = learning_rate

        # Define a simple feedforward neural network
        self.model = nn.Sequential(
            nn.Linear(self.input_size, self.hidden_size),
            nn.ReLU(),
            nn.Linear(self.hidden_size, self.output_size)
        )

        # Define loss function and optimizer
        self.criterion = nn.MSELoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)

        # Set mode to training initially
        self.mode = 'train'

    def step(self, state, action=None, reward=None, return_full_output=False):
        state_tensor = torch.tensor(state, dtype=torch.float32).view(1, -1)
        
        # Set mode for evaluation or training
        if self.mode == 'train':
            self.model.train()  # Set model to training mode
            self.optimizer.zero_grad()  # Clear previous gradients
            output = self.model(state_tensor)  # Get model's prediction

            # If action and reward are provided, calculate loss and update the model
            if action is not None and reward is not None:
                # Ensure action is within the valid range
                if action < 0 or action >= self.output_size:
                    raise ValueError(f"Action ({action}) is out of bounds for output size {self.output_size}")
                
                target = torch.tensor([[reward]], dtype=torch.float32)  # Create target tensor
                loss = self.criterion(output, target)
                loss.backward()  # Backpropagate the error
                self.optimizer.step()  # Update the weights
                return loss.item()  # Return the loss value
            return None  # No loss if not in training mode
        
        elif self.mode == 'output':
            self.model.eval()  # Set model to evaluation mode
            with torch.no_grad():
                output = self.model(state_tensor)  # Get model's prediction
                # If return_full_output is False, return the largest value
                if return_full_output:
                    return output
                else:
                    return output.max().item()  # Return the maximum value as a scalar

    def set_mode(self, mode):
        if mode in ['train', 'output']:
            self.mode = mode
        else:
            raise ValueError("Mode must be either 'train' or 'output'")

    def save(self, path):
        torch.save(self.model.state_dict(), path)  # Save the model's state_dict

    def load(self, path):
        self.model.load_state_dict(torch.load(path, map_location='cpu', weights_only=True))  # Load the model's state_dict
        self.model.eval()  # Set the model to evaluation mode after loading







