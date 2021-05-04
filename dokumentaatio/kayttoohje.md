# Käyttöohje

# Käynnistäminen

Asenna ensin riippuvuudet komennolla `poetry install`.

Käynnistä sitten ohjelma komennolla `poetry run invoke start`

# Pelin ohjeet

Peli alkaa saman tien kun ohjelma käynnistetään.

![](./kuvat/pelin_aloitus.png)

Pelikentälle ilmestyy tetromino, joka putoaa alaspäin. 
Tetrominoa voi ohjata nuolinäppäimillä oikealle ja vasemmalle, kääntää ylänuolella, pudottaa nopeammin alanuolesta sekä pudottaa heti välilyönnillä.

![](./kuvat/taysi_rivi.png)

Kun jokin rivi saadaan täyteen, se poistuu pelikentältä.

![](./kuvat/rivi_poistettu.png)

Peli loppuu, kun uusi tetromino ei enää mahdu ruudulle.


![](./kuvat/pelin_loppuminen.png)
