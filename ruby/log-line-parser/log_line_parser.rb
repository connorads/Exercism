class LogLineParser
  def initialize(line)
    @line = line.split("]: ")[1].strip
    @log_level = line.partition("]")[0].split("[")[1].downcase
  end

  def message
    return @line
  end

  def log_level
    return @log_level
  end

  def reformat
    return "#{@line} (#{self.log_level})"
  end
end
