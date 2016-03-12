#include "application.h"
#include "InternetButton.h"

InternetButton b = InternetButton();

struct Rgb {
    int r;
    int g;
    int b;
};

Rgb getColour(int ledNum);
int flashLed(String ledNumStr);

void setup() {

    Serial.begin(9600);
    Particle.function("flash", flashLed);
    b.begin();
}

void loop() {

}


int flashLed(String ledNumStr) {

    int ledNum = atoi(ledNumStr.c_str());
    Rgb colour = getColour(ledNum);

    Serial.println("Flashing LED " + ledNum);

    b.ledOn(ledNum, colour.r, colour.g, colour.b);
    delay(1000);
    b.ledOff(ledNum);

    return 0;
}

Rgb getColour(int ledNum) {

    if(ledNum == 1) {
        return {100,0,0};
    } else if(ledNum == 2) {
        return {0,100,0};
    } else if(ledNum == 3) {
        return {0,0,100};
    } else {
        return {0,0,0};
    }
}