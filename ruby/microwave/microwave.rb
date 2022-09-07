class Microwave
  attr_reader :timer

  def initialize(input)
    minutes, seconds = input.divmod(100)
    if seconds >= 60
      minutes += 1
      seconds -= 60
    end
    @timer = "%02d:%02d" % [minutes, seconds]
  end
end
