# Um armazém de códigos prontos para métodos numéricos 


Sobre critérios de segurança são formas de estabelecer limites nas iterações, podem ser padronizadas ou avançadas e podem ser aplicadas em todos os métodos

a) Diferença entre iterações dentro de um valor limite (Padrão) ->  Muda de método para método, é como uma identidade 
b) Valor absoluto da função -> Versátil e pode ser usado de forma igual em todos
c) Erro relativo e absoluto -> Responde se um esse erro é grande ou pequeno para o tamanho do valor, dizer se é relevante ou não 

Ex: O ideal é combinar ( Newton-Rapson univariável )
if abs(x_new - x_old) < tol and abs(f(x_new)) < tol:
    break
