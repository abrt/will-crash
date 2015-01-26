class Wrap
  class MyException < Exception
  end
end

class WillClass
  def func
    4.times do
      5.times do
        begin
          8/0
        rescue => e
          raise Wrap::MyException, "Exception\nsuccessfully\nraised."
        end
      end
    end
  end

  begin
    1/0
  rescue ZeroDivisionError
    begin
      3/0
    rescue
      begin
        2/0
      rescue
        3.times do
          a = WillClass.new
          a.func
        end
      end
    end
  end
end
