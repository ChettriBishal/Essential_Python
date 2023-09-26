class Bird {}

class FlyingBird extends Bird {
  fly() {
    console.log('Fyling...');
  }
}

class Eagle extends FlyingBird {
  dive() {
    console.log('Diving...');
  }
}

const eagle = new Eagle();
eagle.fly();
eagle.dive();

class Penguin extends Bird {
  // Problem: Can't fly!
}
/*
According to the Liskov Substitution Principle, 
you should be able to use a Penguin object wherever you use a Bird object without causing problems.
*/