const int buttonPin = A1;
const int buttonPin2 = A2;
int counter = 0;
int tenSec = 10;
int twoMin = 2*60;
int fiveMin = 5*60;
int twentyfiveMin = 25*60;
int thirtyMin = 30*60;

bool timerStarted = false;
unsigned long startTime;
const unsigned long initialTime5 = 2 * 60 * 1000; // 2 minutes for testing

void displayMessage(const char *message)
{
  Serial.println(message);
  delay(1000); // Add a delay to make sure the message is visible before continuing
}

void setup()
{
  Serial.begin(9600);
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(buttonPin2, INPUT_PULLUP);

  // Display initial message
  displayMessage("Press button to start timer");
}
void loop(){
  if (digitalRead(buttonPin) == HIGH && !timerStarted){
    startTimer();
  }

}
void startTimer()
{
  timerStarted = true;
  startTime = millis();
  Serial.print("Timer started: ");
  Serial.print(twentyfiveMin/60);
  Serial.println(":00");
  int x = twentyfiveMin;

  for(int i = 0; i < twentyfiveMin; i++){
    delay(1000);
    x--;

    int minutes = x / 60;
    int seconds = x % 60;

    Serial.print("Remaining: ");
    
    if (minutes < 10) {
      Serial.print("0");
    }
    
    Serial.print(minutes);
    Serial.print(":");
    
    if (seconds < 10) {
      Serial.print("0");
    }
    
    Serial.println(seconds);
  }
}
