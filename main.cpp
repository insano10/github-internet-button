#include "application.h"
#include "InternetButton.h"

InternetButton b = InternetButton();

struct Rgb {
    int r;
    int g;
    int b;
};

Rgb getColour(String notificationType);
int notification(String type);

void setup() {

    Serial.begin(9600);
    Particle.function("notify", notification);
    b.begin();
}

void loop() {

}

int notification(String type) {

    Rgb colour = getColour(type);

    for(int i=0 ; i<10 ; i++) {
        b.spin(colour.r, colour.g, colour.b, 100);
    }
    b.allLedsOff();

    return 0;
}

Rgb getColour(String type) {

    if(type == "PullRequest") {
        return {255,0,255};
    } else if(type == "Push") {
        return {255,165,0};
    } else {
        return {0,0,0};
    }
}