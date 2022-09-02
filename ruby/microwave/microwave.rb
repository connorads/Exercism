class Microwave
  def initialize(seconds)
    @minutes = seconds / 100
    @seconds = seconds % 100
    if @seconds >= 60
      @minutes += 1
      @seconds -= 60
    end
  end

  def timer
    return "#{"%02d" % @minutes}:#{"%02d" % @seconds}"
  end
end
