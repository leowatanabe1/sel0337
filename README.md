O código da tag RFID é bem simples, basicamente definimos leitor como uma classe MFRC522
Depois, basta criar um loop que fica fazendo a leitura da tag, por meio da função .read(), recebendo o id e o texto dentro da tag

Ao ler uma tag, comparamos o id com o id já cadastrado. Se for o mesmo, o acesso é liberado e acende um led verde, caso controário, o acesso é negado e acende umn led vermelho.

---------------------------------------------------------------------------------------------------------------------------

Quanto ao uso da camera, quando fui testar a camera com o comando libcamera-hello, deu o seguinte erro:

WARN V4l2 v4l2_videodevice.cpp:2007 /dev/video0[16:cap]: Dequeue timer of 1000000.00us has expired!
ERROR RPI pipeline_base.cpp: 1333 Camera frontend has timed out!
ERROR RPI pipeline_base.cpp: 1334 Please check that your camera sensor connector is attached securely.
ERROR RPI pipeline_base.cpp: 1335 Alternatively, try another cable and/or sensor.
ERROR: Device timeout detected, attempting a restart!!!

Então como estava com pouco tempo e tava com receio de ter feito a conexão errada, preferi não correr o risco de tentar outros sensores.

----------------------------------------------------------------------------------------------------------------------------

Agora, para a atividade do git, fiz todo o procedimento para 
 
 
