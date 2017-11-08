package edu.ucsd.cs110.temperature;
public class Fahrenheit extends Temperature
{
    public Fahrenheit(float t)
    {
        super(t);
    }

    @Override
    public Temperature toCelsius() {
        float tempConvert = (float) 1.8;
        float newTemp = (this.getValue() - 32)/tempConvert;
        return new Fahrenheit(newTemp);
    }

    @Override
    public Temperature toFahrenheit() {
        return this;
    }

    public String toString()
    {
        // TODO: Complete this method
        return this.getValue() + " F";
    }
}
