class PDController:
    def __init__(self, KP=0.15, KD=0.6):
        self.KP = KP  # Proportional gain
        self.KD = KD  # Derivative gain
        self.previous_error = 0  # Store previous error for derivative calculation

    def compute_control_action(self, reference, output):
        """
        Compute the control action based on the reference and output.
        
        :param reference: Desired reference value (r[t])
        :param output: Actual output value (y[t])
        :return: Control action (u[t])
        """
        error = reference - output  # Calculate the error (e[t])
        control_action = (self.KP * error) + (self.KD * (error - self.previous_error))
        self.previous_error = error  # Update previous error for next iteration
        return control_action