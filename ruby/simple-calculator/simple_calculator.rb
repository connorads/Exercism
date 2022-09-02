class SimpleCalculator
  ALLOWED_OPERATIONS = ["+", "/", "*"].freeze

  class UnsupportedOperation < StandardError
  end

  def self.calculate_string(first_operand, second_operand, operation)
    return "#{first_operand} #{operation} #{second_operand} = #{first_operand.method(operation).(second_operand)}"
  end
  private_class_method :stringify

  def self.calculate(first_operand, second_operand, operation)
    if first_operand.class == String or second_operand.class == String
      raise ArgumentError.new()
    elsif !ALLOWED_OPERATIONS.include?(operation)
      raise UnsupportedOperation.new()
    elsif operation == "+"
      return self.calculate_string(first_operand, second_operand, operation)
    elsif operation == "/"
      if second_operand == 0
        return "Division by zero is not allowed."
      else
        return self.calculate_string(first_operand, second_operand, operation)
      end
    elsif operation == "*"
      return self.calculate_string(first_operand, second_operand, operation)
    end
  end
end
