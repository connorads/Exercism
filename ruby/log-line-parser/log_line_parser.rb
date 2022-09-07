class LogLineParser
  attr_reader :message, :log_level, :reformat

  def initialize(line)
    @message = line.split("]: ")[1].strip
    @log_level = line.partition("]")[0].split("[")[1].downcase
    @reformat = "#{@message} (#{@log_level})"
  end
end
