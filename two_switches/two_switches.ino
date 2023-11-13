const int buttonPin = A1;
const int buttonPin2 = A3;
int counter = 1;
bool counterStarted = false;
unsigned long startTime;
const unsigned long initialTime = 25 * 60 * 1000;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(buttonPin2, INPUT_PULLUP);
}

void loop() {
  // Start counter button
  if (digitalRead(buttonPin) == LOW && !counterStarted) {
    counterStarted = true;
    // Serial.println("Counter started");
  }

  // Increment counter if counter has started
  if (counterStarted && digitalRead(buttonPin) == HIGH) {
    
    Serial.print("Counter: ");
    Serial.println(counter);
    counterStarted = false; 
    counter++;
  }

  // Reset button
  if (digitalRead(buttonPin2) == HIGH) {
    counter = 0;
    Serial.println("Counter reset");
    delay(1000); // Delay to debounce the reset button
  }

  delay(50); // Debouncing delay to avoid rapid counting
}
