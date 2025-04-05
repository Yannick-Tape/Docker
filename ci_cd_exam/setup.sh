#!/bin/bash

echo " Suppression des anciens containers..."
docker-compose down

echo " Construction des images..."
docker-compose build

echo "Lancement des tests..."
docker-compose up

