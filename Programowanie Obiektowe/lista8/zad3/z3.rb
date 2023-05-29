#Karolina Jędraszek
#lista 8 zadanie 3
#ruby 3.2.2
class ONPExpr
  def initialize(expression) #table that represents an expression
    @expression = expression
    @stack = []
  end

  def oblicz(variables) #var is a dictionary that contains variables and their values
    @expression.each do |element|
      case element
      when Integer
        @stack.push(element)
      when '+', '-', '*', '/'
        perform_operation(element)
      when String
        @stack.push(variables[element])
      end
      puts @stack.inspect
    end
    @stack.pop
  end

  private

  def perform_operation(operator)
    if @stack.size < 2
        print ("Error, the given expression is not correct")
    else
        operand2 = @stack.pop
        operand1 = @stack.pop
        result = case operator
                when '+'
                operand1 + operand2
                when '-'
                operand1 - operand2
                when '*'
                operand1 * operand2
                when '/'
                operand1 / operand2
                end
        @stack.push(result)
    end
  end
end

#----------------------------------------
print("Test1 (1 + 2)*3:\n")
t1 = [1, 2, '+', 3, '*']
e1 = ONPExpr.new(t1)
d1 = {}
print(e1.oblicz(d1))
puts "\n\n"

print("Test2 (x - y) / 5:\n")
t2 = ['x', 'y', '-', 5, '/']
e2 = ONPExpr.new(t2)
d2 = {}
d2['x'] = 25
d2['y'] = 5
print(e2.oblicz(d2))
