# Lab 3

### Objectives

- Use `input` to get input from a user.
- Cast a `string` to an `integer`.
- Use `try/except` to capture invalid inputs.
- Practice the use of the `if/else` statement.
- Practice the use of a `while` loop.

### Resources

- To import the adafruit library you use the following statement at the start of your code
  `from adafruit_circuitplayground import cp`
  
- Use:
  `blue = (0,0,255)`
  to initialize the variable `blue` to the color blue (using a `tuple`)
  
- Use the following `for` loop to switch off all the leds.

  ```
  #Turn off the leds
      for i in range(10):
          cp.pixels[i]=(0,0,0)
  ```

  

### Code to write 

1. Download the program `lab3.py`

   - In Pycharm or Visual studio code, open `lab3.py`.

   - Run the code.

   - When prompted enter different values for the number of LEDs so that you test the code thoroughly.

2. Run the code again and enter a string when prompted for the number of LEDs.
   - Run the code and check that the program crashes.
   - Use a `try .. except` block to protect line 4 from invalid inputs.
   - Test your code by entering characters, float, anything and make sure it is now protected against invalid inputs.
3. Connect your Circuit Playground (CP) to your laptop.
   - Open Visual Studio the open the CP folder.
   - Save your file `lab3.py` to the CP as `code.py` then run the code to check it is still working on the CP.
   - Import the adafruit library at the top of your program.
   - Replace the line `print("LED {} is ON".format(i))` with the code that turns the LEDS in blue.
   - At the end of your program, add the code to  all the LEDs off.
   - Test your code thoroughly.
   - At the end of your program, add the code to  all the LEDs off.
   - Test your code thoroughly.
4. At the start of your code, add a block comment to identify you and to explain in plain english what your code does.

### Submission

Upload the two programs `lab3.py` and `code.py` to Github. 

Identify yourself using the txt file.




