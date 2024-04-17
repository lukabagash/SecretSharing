Luka Bagashvili

The projects contains:

data folder: containing random numbers generated in case reconstructing precise experiment based on same input.

docs: containing the result implications and a README.

results: containing a graphs folder and exact runtimes in txt files with accuracy.

src: 

    main.py: this file should be executed in order to reproduce the results.

    no_privacy_computation.py: no privacy setting.

    pallier.py: computation of the average with cryptography.

    shamir_secret_sharing.py: shamir method.

    differential_privacy.py: differential privacy method.

    utilities: random number generator, the time counter which can run several times and calculate average
               of the times to calculate more precise runtime.