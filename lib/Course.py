class Course:
  def __init__(self, title=None, schedule=None, description=None):
    self.title = title
    self.schedule = schedule
    self.description = description

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def schedule(self):
        return self._schedule
    
    @schedule.setter
    def schedule(self, value):
        self._schedule = value

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value


  def __str__(self):
    output = ''
    output += f'Title: {self.title}\nSchedule: {self.schedule}\nDescription: {self.description}\n'
    output += '------------------'
    return output
