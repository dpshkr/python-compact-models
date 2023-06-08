# python-compact-models

A collection of semiconductor compact models in Python. 
These models are helpful for quickly benchmarking experimental data and building blocks of more complex models.

## Common usage pattern

Using these models is extremely simple. 
All models depend only on `numpy` and `scipy` libraries. 
No other libraries are required.
Each compact model is represented by a class. 
Using each model is a two-step process -

### Instantiate the model

```python
m = FETModel(paramaters)
```

Here `parameters` is a dictionary containing the set of input parameters, 
usually material or device properties like mobility gate insulator thickness, etc. 
The details of the parameters are model dependent and are given in further sections.
For all the models, some default values of these parameters are assumed so that all parameters are optional.

### Apply bias

Once the model is instantiated, call the `apply_bias` method of the object to obtain the drain current.

```python
Id = m.apply_bias(VG, VD)
```

Here `VG` and `VD` are gate and drain bias respectively (in Volts).
`Id` is the drain current in amperes per meter.

## Double-gate MOSFET with undoped body

This class `DGFET` implements the model of an undoped double gate MOSFET as described in [1].

## References

1. Taur, Yuan, et al. "A continuous, analytic drain-current model for DG MOSFETs." *IEEE Electron Device Letters* 25.2 (2004): 107-109.




