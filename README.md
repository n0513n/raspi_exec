🇧🇷 raspi_exec
---

### raspberry-pi_exec

Script utilizado para monitorar uma porta [GPIO](https://www.raspberrypi.org/documentation/usage/gpio/) por mudanças de estado para executar comandos remotamente.

Desenvolvido em parceria com [Diego Kern Lopes](https://diegokernlopes.com/) ([Organon-Ufes](http://organon.ufes.br/)). Testado com o modelo Raspberry Pi 3b.

### Requisitos

* **Python 2.7+/3.6+**
* RPi.GPIO

A biblioteca RPi.GPIO vem instalada por padrão nos sistemas [Raspbian](https://www.raspbian.org/).

### Execução

Execute o comando a seguir no terminal de seu Raspberry para iniciar o script **após configurá-lo**:

```python raspi_exec.py```

### Configuração

#### Parâmetros de configuração

As opções de execução podem ser definidas para importação no arquivo ```config.py``` (exemplo incluso):

* **CMD**: comando padrão para executar
* **PORT**: porta GPIO para monitorar (padrão: 40)
* **CMD_CHECK**: comando para checar output (padrão: nenhum)
* **CMD_START**: comando para executar no começo (padrão: nenhum)
* **RECHECK**: segundos para re-executar CMD_CHECK (padrão: 0)
* **WAIT**: segundos de espera para loop (padrão: 0.25)
* **DEFAULT**: estado inicial da porta (padrão: False)
* **SCREEN**: tela para executar comando (padrão: "DISPLAY=:0")

#### Ativando hotspot WiFi (opcional)

Alguns modelos de Raspberry podem criar uma rede hotspot para conectar-se sem fio a outros computadores.

Uma opção para facilmente habilitá-la, **se suportado**, é instalando-se o software [RaspAP](https://github.com/billz/raspap-webgui):

```wget -q https://git.io/voEUQ -O /tmp/raspap && bash /tmp/raspap```

As configurações padrão após a instalação são as seguintes:

* Endereço IP: 10.3.141.1
    * Usuário: admin
    * Senha: secret
* Intervalo DHCP: 10.3.141.50 - 10.3.141.255
* SSID: raspi-webgui
* Senha: ChangeMe

Recomenda-se configurar a rede WiFi a partir da interface gráfica disponível por padrão no endereço IP acima.

**Nota:** qualquer conexão sem fio ou cabeada serve para comunicação entre computadores, desde que estejam numa mesma rede.

#### Controle remoto por SSH (opcional)

Para instalar os pacotes em sistemas Debian/Raspbian/Ubuntu e derivados:

```sudo apt install openssh-server wmctrl xdotool```

O pacote *wmctrl* pode ser utilizado para interagir com janelas (X) e *xdotool* para enviar comandos, e.g. teclas.

### Referência

* [GPIO - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/usage/gpio/)