from selenium import webdriver


navegador = webdriver.Chrome()

#Acesso ao site
navegador.get("http://www.ssp.sp.gov.br/Estatistica/Pesquisa.aspx")
#Acesso á Ocorrências registradas por mês
navegador.find_element_by_xpath('//*[@id="conteudo_btnMensal"]').click()
#Acesso a Capital
navegador.find_element_by_xpath('//*[@id="conteudo_repLateral_lkLateral_0"]').click()
# Download  arquivo Capital
navegador.find_element_by_xpath('//*[@id="conteudo_btnExcel"]').click()


#para poder voltar prt1
navegador.find_element_by_xpath('//*[@id="conteudo_lkEstado"]').click()


#Acesso a São José dos Campos
navegador.find_element_by_xpath('//*[@id="conteudo_repLateral_lkLateral_2"]').click()
#Download do arquivo de São José dos Campos
navegador.find_element_by_xpath('//*[@id="conteudo_btnExcel"]').click()


#para poder voltar prt2
navegador.find_element_by_xpath('//*[@id="conteudo_lkEstado"]').click()


#Acesso a Campinas
navegador.find_element_by_xpath('//*[@id="conteudo_repLateral_lkLateral_3"]').click()
#Download do arquivo de Campinas
navegador.find_element_by_xpath('//*[@id="conteudo_btnExcel"]').click()


#para poder voltar prt3
navegador.find_element_by_xpath('//*[@id="conteudo_lkEstado"]').click()


#Acesso a Riberão Preto
navegador.find_element_by_xpath('//*[@id="conteudo_repLateral_lkLateral_4"]').click()
#Download do arquivo de Ribeirão Preto
navegador.find_element_by_xpath('//*[@id="conteudo_btnExcel"]').click()


#para poder voltar ptr4
navegador.find_element_by_xpath('//*[@id="conteudo_lkEstado"]').click()


#Acesso a Bauru
navegador.find_element_by_xpath('//*[@id="conteudo_repLateral_lkLateral_5"]').click()
#Download do arquivo de Bauru
navegador.find_element_by_xpath('//*[@id="conteudo_btnExcel"]').click()


#para poder voltar ptr5
navegador.find_element_by_xpath('//*[@id="conteudo_lkEstado"]').click()


#Acesso a São José do Rio Preto
navegador.find_element_by_xpath('//*[@id="conteudo_repLateral_lkLateral_6"]').click()
#Download do arquivo de José do Rio Preto
navegador.find_element_by_xpath('//*[@id="conteudo_btnExcel"]').click()


#para poder voltar ptr6
navegador.find_element_by_xpath('//*[@id="conteudo_lkEstado"]').click()


#Acesso a Santos
navegador.find_element_by_xpath('//*[@id="conteudo_repLateral_lkLateral_7"]').click()
#Download do arquivo de Santos
navegador.find_element_by_xpath('//*[@id="conteudo_btnExcel"]').click()


#para poder voltar ptr7
navegador.find_element_by_xpath('//*[@id="conteudo_lkEstado"]').click()


#Acesso a Sorocaba
navegador.find_element_by_xpath('//*[@id="conteudo_repLateral_lkLateral_8"]').click()
#Download do arquivo de Sorocaba
navegador.find_element_by_xpath('//*[@id="conteudo_btnExcel"]').click()


#para poder voltar ptr8
navegador.find_element_by_xpath('//*[@id="conteudo_lkEstado"]').click()


#Acesso a Presidente Prudente
navegador.find_element_by_xpath('//*[@id="conteudo_repLateral_lkLateral_9"]').click()
#Download do arquivo de Presidente Prudente
navegador.find_element_by_xpath('//*[@id="conteudo_btnExcel"]').click()


#para poder voltar ptr9
navegador.find_element_by_xpath('//*[@id="conteudo_lkEstado"]').click()


#Acesso a Piracicaba
navegador.find_element_by_xpath('//*[@id="conteudo_repLateral_lkLateral_10"]').click()
#Download do arquivo de Piracicaba
navegador.find_element_by_xpath('//*[@id="conteudo_btnExcel"]').click()


#para poder voltar ptr10
navegador.find_element_by_xpath('//*[@id="conteudo_lkEstado"]').click()


#Acesso a Araçatuba
navegador.find_element_by_xpath('//*[@id="conteudo_repLateral_lkLateral_11"]').click()
#Download do arquivo de Araçatuba
navegador.find_element_by_xpath('//*[@id="conteudo_btnExcel"]').click()

