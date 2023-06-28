# <DOCTYPE html>
# <html>
#   <body>
#     <h1>Assignment-3</h1>
#     <p>
      def find_max(numbers):
          max_number = 0
          for i in range(len(numbers)):
              if numbers[i] > max_number:
                  max_number = numbers[i]
          return max_number
      
      def find_position(numbers, target):
          list_position = []
          for i in range(len(numbers)):
              if numbers[i] == target:
                  list_position.append(i)
          if not list_position:
              list_position.append(-1)
          return list_position[0]
#     </p>
#   <body>
# </html>
