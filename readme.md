# Makin' Lists

An intelligent way to start makin' your grocery or shopping list.

## The Obvious
This is a list organization tool brought about by the less than pleasant experience of using built in notepad apps as a list tool for makin' groceries.

## Lists
Grocery lists are made using one of all of the following ways:

1.  Adding items one by one
2.  Adding meals that the user has set up (think recipe)
3.  Temporally based suggestions of low recurring items (ex: dish soap, towels, dog food)

These are the current spec, but that could change. This process is designed to be done in a browser or a smartphone.

## Makin' Groceries
The grocery makin' process is pretty terrible, especially when you're at a store with questionable produce.

Anyway, the implimentaiton is designed to be used on a smartphone with intelligently sized buttons that are easily recognized as **need to buy** and **already in the basket**.

There are some fun things goin on in the background.  The order of marking is recorded, so the app gets smarter based on buying habits so the list is ordered the next time the app is run. Geolocation is not part of the spec, but could easily be used as a precursor to the list ordering due to unique store configuration.

## The Bill
This app is a learning tool for the design team, but any funds would initally be scaled to the cost of deployment

## Technology Stack
Extensive use of python will likely be used due to the team's familiarity.

Backend work will likely use postgres to store user info, shopping lists, recipes, and any additional data needed for the app.

This database,application, and front end will be built with django.

## Documentation
all documentation will be done with Sphinx.