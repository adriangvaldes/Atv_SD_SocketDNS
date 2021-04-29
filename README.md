# Atv_SD_SocketDNS

Nossa estratégia para resolução do problema foi colocar todos os trabalhos em relação ao IP dos servers em um componentes separado, que chamamos de `dns.py` onde nele possui toda a loja para o tratamento dos endereços. O cliente apenas envia o array desejado e o elemento a ser buscado no array, dividindo este em duas partes (uma para cada servidor, que neste caso foi escolhido ser dois servidores, tendo a possibilidade de aumentar essa quantidade futuramente). Importante ressaltar que o cliente não necessita fazer nada manualmente, tudo ocorre de maneira automática.
