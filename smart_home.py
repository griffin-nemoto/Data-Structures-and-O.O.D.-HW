class SmartDevice:
    def __init__(self, name:str):
        '''Initializes device with name from input and sets status to off
        Parameters: name (str)
        Returns: None
        '''
        self.name = name
        self.status = False

    def turn_on(self):
        '''Sets device status to on
        Parameters: None
        Returns: None
        '''
        self.status = True

    def turn_off(self):
        '''Sets device status to off
        Parameters: None
        Returns: None
        '''
        self.status = False

    def __str__(self):
        '''Returns name and status of device
        Parameters: None
        Returns: name and status of device (str)'''
        if self.status:
            return f'{self.name}: ON'
        else:
            return f'{self.name}: OFF'
class Light(SmartDevice):
    brightness = 100

    def adjust_brightness(self, level):
        '''Sets new value for brightness
        Parameters: level (int)
        Returns: None
        '''
        self.brightness = level
    
    def __str__(self):
        '''Returns description of object
        Parameters: None
        Returns: object's name, status, and brightness (str)
        '''
        #Add brightness level to SmartDevice's __str__ function to reduce repetition
        return f'{super().__str__()}, Brightness: {self.brightness}'
    
class Thermostat(SmartDevice):
    temperature: float = 65
    
    def adjust_temperature(self, temp):
        '''Sets new temperature based on input if between 55-80 degrees Fahrenheit
        Parameters: temp (float)
        Returns: None
        '''
        if self._check_temperature_limits(temp):
            self.temperature = temp
    
    def __str__(self):
        '''Returns description of object
        Parameters: None
        Returns: Object's name, status, and temperature
        '''
        return f'{super().__str__()}, Temperature: {self.temperature}'
    
    def _check_temperature_limits(self, temp):
        '''Checks if given temperature is within valid range(55-80 degrees F)
            Private method
        Parameters: temp (float)
        Returns: Bool
        '''
        return 55<=temp and temp<=80
    
class Speaker(SmartDevice):
    volume: int =  3
    def increase_volume(self):
        '''Increases volume by 1, max of 10
        No Parameters or Return
        '''
        if self.volume < 10:
            self.volume += 1
    
    def decrease_volume(self):
        '''Decreases volume by 1, min of 1
        No Parameters or Return
        '''
        if self.volume > 1:
            self.volume -= 1
    def __str__(self):
        '''Returns description of with object's name, status, and volume'''
        return f'{super().__str__()}, Volume: {self.volume}'
    
class SmartHome:
    def __init__(self):
        self.devices = []
    def __add__(self, other):
        '''Adds SmartDevice object to 'devices' list
        Parameters: other (SmartDevice)
        Returns: None
        '''
        if isinstance(other,list):
            self.devices.extend(other)
        else:
            self.devices.append(other)
        return self
    
    def turn_off_all(self):
        '''Turns off all devices in 'devices' 
        No Parameters or returns
        '''
        for device in self.devices:
            device.turn_off()
    
    def __str__(self):
        '''Returns name and status of all devices in 'devices' 
        No parameters
        '''
        device_string:str = ''
        #Concatenates each device's information to device_string
        for device in self.devices:
            if device.status:
                device_string += f'{device.name}: ON, '
            else:
                device_string += f'{device.name}: OFF, '
        return device_string