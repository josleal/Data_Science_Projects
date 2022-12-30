
metricas_lm <- function(modelo){
  # thus the degrees of freedom r uses are 12 instead of 11
  
  loglik <- logLik(modelo)
  n   <- attributes(loglik)$nobs # following user20650 recommendation 
  p   <- attributes(loglik)$df # following user20650 recommendation
  dev <- -2*as.numeric(loglik)
  aic  <- dev + 2 * p
  aicc <- aic + (2 * p^2 + 2 * p)/(n - p - 1)
  bic  <- dev +  p * log(n)
  
  return(
    cat("AIC  =",aic,
        "\nBIC  =", bic,
        "\nAICc =", aicc))
  
}





