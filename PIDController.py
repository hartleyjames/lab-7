from math import sqrt


class PIDController:

    def __init__(self, k_p, k_i, k_d, num_time_steps=5):
        self.k_p = k_p
        self.k_i = k_i
        self.k_d = k_d
        self.prev_error_list = [0] * num_time_steps
        self.num_time_steps = num_time_steps
        self.previous_error = 0
        self.error_list_counter = 0

    def updateInputValue(self, err):
        # calls the functions below and adds their result
        processed_error = self.__error_function__(err)
        self.previous_error = processed_error
        p_term = self.__proportional_controller__(processed_error)
        i_term = self.__integral_controller__(processed_error)
        d_term = self.__derivative_controller__(processed_error)
        self.error_list_counter += 1
        return p_term + i_term + d_term

    def __error_function__(self, error):
        print("This error function was not supposed to be called!")
        return error  # not intended to be run

    def __proportional_controller__(self, err):
        return self.k_p * err

    def __integral_controller__(self, err):
        self.prev_error_list[self.error_list_counter % self.num_time_steps] = err
        return self.k_i * sum(self.prev_error_list)

    def __derivative_controller__(self, err):
        return self.k_d * (err - self.previous_error)


class LinearSpeedPIDController(PIDController):

    def __error_function__(self, error):
        """
        Needs to calculate a new p term based on a unique error function for controlling linear speed
        For this class, the error might be the distance from the goal

        :param error:
        :return float:
        """
        return error / 2


class AngularSpeedPIDController(PIDController):

    def __error_function__(self, error):
        """
        Needs to calculate a new p term based on a unique error function for controlling angular speed
        For this class, the error might be the target's number of pixels away from the center of the camera

        :param error:
        :return:
        """
        return error / 2


if __name__ == "__main__":
    lpid1 = LinearSpeedPIDController(0.1, 0.1, 0, 5)
    values_to_test = [200, 150, 100, 50, 25, 15, 10, 5]
    for value in values_to_test:
        return_val = lpid1.updateInputValue(value)
        print return_val
    print
    lpid2 = LinearSpeedPIDController(0.2, 0.15, 0, 5)
    for value in values_to_test:
        return_val = lpid2.updateInputValue(value)
        print return_val
    print
    apid = AngularSpeedPIDController(0.2, 0.15, 0, 5)
    for value in values_to_test:
        return_val = apid.updateInputValue(value)
        print return_val
    exit()
