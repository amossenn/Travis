package edu.ucsd.cs110.temperature;

public class Celsius extends Temperature
{
    public Celsius(float t)
    {
        super(t);
    }

    @Override
    public Temperature toCelsius(){
        return this;
    }

    @Override
    public Temperature toFahrenheit() {
        float tempConvert = (float) 1.8;
        float newTemp = (this.getValue() * tempConvert) + 32;
        return new Celsius(newTemp);
    }

    public String toString()
    {
        // TODO: Complete this method
        return this.getValue() + " C";
    }
}