---
title: "Statistical distribution functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalDistributionFunctions/statistical-distribution-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---

# Statistical distribution functions

Expand/Collapse all

# Statistical distribution functions

Statistical distribution functions return the probabilities of occurrence of different possible outcomes for a given input [variable](#glossary-0 "Glossary term"). You can use these functions to calculate the potential values of your data points.

The three groups of statistical distribution functions described below are all implemented in Qlik Sense using the Cephes function library. For references and details on algorithms used, accuracy, and so on, see: [Cephes library](http://www.netlib.org/cephes/).
The Cephes function library is used by permission.

- The probability functions calculate the probability at the point in the distribution given by the supplied value.

  - The Frequency functions are used for discrete distributions.
  - The Density functions are used for continuous functions.
- The Dist functions calculate the accumulated probability of the distribution at the point in the distribution given by the supplied value.
- The Inv functions calculate the inverse value, given the accumulated probability of the distribution.

All functions can be used in both the data [load script](#glossary-1 "Glossary term") and in chart expressions.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

BetaDensity

BetaDensity() returns the probability of the Beta distribution.

[**BetaDensity**](BetaDensity.htm)(value, alpha, beta)

BetaDist

BetaDist() returns the accumulated probability of the Beta distribution.

[**BetaDist**](BetaDist.htm)(value, alpha, beta)

BetaInv

BetaINV() returns the inverse of the accumulated probability of the Beta distribution.

[**BetaInv**](BetaInv.htm)(prob, alpha, beta)

BinomDist

BinomDist() returns the accumulated probability of the Binomial distribution.

[**BinomDist**](BinomDist.htm)(value, trials, trial\_probability)

BinomFrequency

BinomFrequency() returns the Binomial probability distribution.

[**BinomFrequency**](BinomFrequency.htm)(value, trials, trial\_probability)

BinomInv

BinomInv() returns the inverse of the accumulated probability of the Binomial distribution.

[**BinomInv**](BinomInv.htm)(prob, trials, trial\_probability)

ChiDensity

ChiDensity() returns the one-tailed probability of the chi2 distribution. The chi2 density function is associated with a chi2 test.

[**ChiDensity**](ChiDensity.htm)(value, degrees\_freedom)

ChiDist

ChiDist() returns the one-tailed probability
of the chi2 distribution. The chi2 distribution is associated with a chi2 test.

[**ChiDist**](ChiDist.htm)(value,
degrees\_freedom)

ChiInv

ChiInv() returns the inverse of the one-tailed
probability of the chi2 distribution.

[**ChiInv**](ChiInv.htm)(prob,
degrees\_freedom)

FDensity

FDensity() returns the probability of the F distribution.

[**FDensity**](FDensity.htm)(value, degrees\_freedom1, degrees\_freedom2)

FDist

FDist() returns the accumulated probability of the F distribution.

[**FDist**](FDist.htm)(value,
degrees\_freedom1, degrees\_freedom2)

FInv

FInv() returns the inverse of the accumulated probability of the F distribution.

[**FInv**](FInv.htm)(prob, degrees\_freedom1,
degrees\_freedom2)

GammaDensity

GammaDensity() returns the probability of the Gamma distribution.

[**GammaDensity**](GammaDensity.htm)(value, k, θ)

GammaDist

GammaDist() returns the accumulated probability of the Gamma distribution.

[**GammaDist**](GammaDist.htm)(value, k, θ)

GammaInv

GammaInv() returns the inverse of the accumulated probability of the Gamma distribution.

[**GammaInv**](GammaInv.htm)(prob, k, θ)

NormDist

NormDist() returns the cumulative normal
distribution for the specified mean and standard deviation. If mean = 0
and standard\_dev = 1, the function returns the standard normal distribution.

[**NormDist**](NormDist.htm)(value,
mean, standard\_dev)

NormInv

NormInv() returns the inverse of the normal
cumulative distribution for the specified mean and standard deviation.

[**NormInv**](NormInv.htm)(prob,
mean, standard\_dev)

PoissonDist

PoissonDist() returns the accumulated probability of the Poisson distribution.

[**PoissonDist**](PoissonDist.htm)(value, mean)

PoissonFrequency

PoissonFrequency() returns the Poisson probability distribution.

[**PoissonFrequency**](PoissonFrequency.htm)(value, mean)

PoissonInv

PoissonInv() returns the inverse of the accumulated probability of the Poisson distribution.

[**PoissonInv**](PoissonInv.htm)(prob, mean)

TDensity

TDensity() returns the value for the student's t density function where a numeric value is a calculated value of t for which the probability is to be computed.

[**TDensity**](TDensity.htm)(value, degrees\_freedom, tails)

TDist

TDist() returns the probability for the
student's t distribution where a numeric value is a calculated value of t for which the probability is to be computed.

[**TDist**](TDist.htm)(value,
degrees\_freedom, tails)

TInv

TInv() returns the t value of the student's
t distribution as a function of the probability and the degrees of freedom.

[**TInv**](TInv.htm)(prob, degrees\_freedom)

## Learn more

- [*Statistical aggregation functions*](../StatisticalAggregationFunctions/statistical-aggregation-functions.htm)
