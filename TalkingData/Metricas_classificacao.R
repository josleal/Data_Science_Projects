

# RELATÓRIO DAS MÉTRICAS

# Inserir a matriz de confusão no formato:
# table(Previsto = previsao_svm, Referencia = dados_teste_normalizado$classe)

# Exemplo se positive = "0":
#         Reference
# Previsto  0 1
#         0 0 3
#         1 1 2

# Exemplo:
#         Reference
# Previsto  0    1
#         0 VP  FP
#         1 FN  VN


# Exemplo se positive = "1":
#         Reference
# Previsto  0 1
#         0 2 1
#         1 3 0

# Exemplo:
#         Reference
# Previsto  0    1
#         0 VN  FN
#         1 FP  VP

metricas_class <- function(positive, matriz_confusao, titulo){
  
  
  if (positive == 0 | positive == "A"){
    # Exemplo:
    #         Reference
    # Previsto  0    1
    #         0 VP  FP
    #         1 FN  VN
    
    acuracia <- (matriz_confusao[1,1] + matriz_confusao[2,2])/(matriz_confusao[1,1] + matriz_confusao[2,2] + matriz_confusao[1,2] + matriz_confusao[2,1])
    recall <- matriz_confusao[1,1]/(matriz_confusao[1,1] + matriz_confusao[2,1])
    precisao <- matriz_confusao[1,1]/(matriz_confusao[1,1] + matriz_confusao[1,2])
    especificidade <- matriz_confusao[2,2]/(matriz_confusao[1,2] + matriz_confusao[2, 2])}

  if (positive == 1 | positive == "B"){
    # Exemplo:
    #         Reference
    # Previsto  0    1
    #         0 VN  FN
    #         1 FP  VP
    
    acuracia <- (matriz_confusao[2,2] + matriz_confusao[1,1])/(matriz_confusao[1,1] + matriz_confusao[2,2] + matriz_confusao[1,2] + matriz_confusao[2,1])
    recall <- matriz_confusao[2,2]/(matriz_confusao[2,2] + matriz_confusao[1,2])
    precisao <- matriz_confusao[2,2]/(matriz_confusao[2,2] + matriz_confusao[2,1])
    especificidade <- matriz_confusao[1,1]/(matriz_confusao[2,1] + matriz_confusao[1, 1])}
    
    
  f1_score <- 2 * precisao * recall/(precisao + recall)
  
  return (
    cat(titulo,
        "\n",
        "\nAcuracia (Accuracy)          =", round(acuracia,4),
        "\nRecall (Sensitivity)         =", round(recall,4),
        "\nPrecisao (Precision)         =", round(precisao,4),
        "\nF1 Score (F-Score)           =", round(f1_score,4),
        "\nEspecificidade (Specificity) =", round(especificidade,4)))
}






