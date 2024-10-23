class ClosedLoop:
    def __init__(self, submarine, controller):
        self.submarine = submarine
        self.controller = controller

    def simulate(self, reference_signal, disturbances):
        """
        Simulate the control loop for a given reference signal with disturbances.
        
        :param reference_signal: Array of reference values (r[t])
        :param disturbances: Array of disturbances to add to the output (y[t])
        """
        outputs = []  # Store output values (y[t])
        control_actions = []  # Store control actions (u[t])
        
        for t in range(len(reference_signal)):
            current_output = self.submarine.get_depth()  # Assume this method exists
            disturbance = disturbances[t] if t < len(disturbances) else 0
            current_output += disturbance  # Apply disturbance to output
            
            control_action = self.controller.compute_control_action(reference_signal[t], current_output)
            control_actions.append(control_action)
            
            # Update submarine with the control action (assuming a method to set control)
            self.submarine.set_control(control_action)
            new_depth = self.submarine.update()  # Update submarine state
            outputs.append(new_depth)
        
        return outputs, control_actions
