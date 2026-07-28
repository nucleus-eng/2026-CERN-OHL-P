# Protocol: PH Measurement using BCECF in Cell-Free Systems

The ratiometric fluorescent probe BCECF is widely employed for monitoring internal pH due to its pKa of approximately 7.0, which ensures high sensitivity within the physiological range [Rink et al., 1982]. By determining the ratio of fluorescence emission at 535 nm from dual excitation at 490 nm and 440 nm,  the pH can be measured independently of the absolute fluorescence intensity.

## Reagent Preparation
- Stock Solution: Resuspend the BCECF powder (Biotium, Product# 51010, 1 mg, MW 520 g/mol) in MilliQ water to a final concentration of 10 mM.
- Working Solution: Dilute the stock solution in MilliQ water to reach a 100 µM concentration.
- Storage: Store both solutions at 4°C, protected from light.

## Sample Preparation (myTXTL Mix)
- Thaw one tube of myTXTL (Arbor Bioscience, myTXTL) on ice.
- Add the DNA template to reach a final concentration of 5 nM.
- Adjust the volume with MilliQ water to reach 90% of the target final volume.
- Add the 100 µM BCECF solution to reach a final concentration of 10 µM (completing the remaining 10% of the volume).
- Mix gently by pipetting up and down.
- Briefly spin down the tube to collect the mixture and remove air bubbles.

## Plate Loading and Measurement
- Dispense 2 µL of the mixture per well into a 96-well plate (NEST, Product# SKU701211).
- Place the plate into the Neo2 plate reader.
- Kinetics Settings: Run a 24-hour kinetic assay with measurements every 3 minutes at gain 40 ms.
- Fluorescence Parameters: Perform ratiometric imaging using the following excitation/emission pairs:
    - 440 nm / 520 nm
    - 490 nm / 520 nm 

## Data Analysis
- Process the raw fluorescence data by calculating the ratio of the two signals
- Convert the ratio values into pH measurements using a pre-established calibration curve.
