
# This script was written by Chibuzo Ukegbu
# As part of the paper verification benchmarks for cooperative verification of  PLC"

#!/bin/bash

echo "This is a demonstration of the custom verifier validator"
echo " that validates a verifier using two other verifiers"

echo "########################################"
echo "Custom_verifier_validator, as demonstrated in the paper"
echo "########################################"

# Get the path to the folder containing the files
folder_path="./test-data/programs"

# Find all the regular files in the folder
files=$(find "$folder_path" -type f)

# Create a for loop to iterate over the list of files
for file in $files; do
  # Execute the coveriteam command for the current file
  ../bin/coveriteam customVerifier_validator.cvt \
    --input verifier_path=../actors/symbiotic.yml \
    --input verifier_version=default \
    --input validator1_path=../actors/pesco.yml \
    --input validator1_version=default \
    --input validator2_path=../actors/cbmc.yml \
    --input validator2_version=default \
    --input program_path="$file" \
    --input specification_path=test-data/properties/unreach-call.prp \
    --input data_model=ILP32
done
echo"##########################################"
echo" End of verification with safety property"
echo"##########################################"


echo"##########################################"
echo" Start of verification with security property"
echo"##########################################"

folder_path="./test-data/programs"

# Find all the regular files in the folder
files=$(find "$folder_path" -type f)

# Create a for loop to iterate over the list of files
for file in $files; do
  # Execute the coveriteam command for the current file
  ../bin/coveriteam customVerifier_validator.cvt \
    --input verifier_path=../actors/symbiotic.yml \
    --input verifier_version=default \
    --input validator1_path=../actors/pesco.yml \
    --input validator1_version=default \
    --input validator2_path=../actors/cbmc.yml \
    --input validator2_version=default \
    --input program_path="$file" \
    --input specification_path=test-data/properties/no-overflow.prp \
    --input data_model=ILP32
done

echo"##########################################"
echo" End of verification with security property"
echo"##########################################"




