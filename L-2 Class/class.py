class Car:
    colour = "Red"
    model = "tesla"

    def cal_avg_speed(self, km=4, time=6):
        speed = time*km
        return self.colour, self.model, speed


model = Car()
print(model.cal_avg_speed())
