### **README.md**

# Star Escape 🚀

Bem-vindo ao **Star Escape**, um jogo onde você controla uma nave espacial e precisa desviar de inimigos para sobreviver o máximo de tempo possível! Vamos aprender como jogar, como o jogo funciona e como você pode executá-lo no seu computador.

---

## **Como Jogar**
1. Use as **setas do teclado**:
   - **Seta para a esquerda**: Move a nave para a esquerda.
   - **Seta para a direita**: Move a nave para a direita.
2. **Objetivo**:
   - Desvie dos inimigos que caem do topo da tela.
   - Sobreviva o máximo de tempo possível!
3. **Quando você colidir com um inimigo**:
   - O jogo termina.
   - Você verá sua pontuação e o tempo que sobreviveu.
   - Você pode escolher reiniciar o jogo ou sair.

---

## **Como Instalar e Executar o Jogo**
Siga estas etapas para jogar no seu computador:

### **1. Instale o Python**
- Certifique-se de que o Python 3 está instalado no seu computador.
- Para verificar, abra o terminal ou prompt de comando e digite:
  ```bash
  python --version
  ```
- Se não estiver instalado, baixe e instale o Python em [python.org](https://www.python.org/).

### **2. Instale o Pygame**
- O jogo usa a biblioteca **Pygame**. Para instalá-la, digite este comando no terminal:
  ```bash
  pip install pygame
  ```

### **3. Baixe os Arquivos do Jogo**
- Certifique-se de que você tem os seguintes arquivos e pastas:
  ```
  StarEscape/
  ├── assets/
  │   ├── player.png
  │   ├── enemy.png
  │   ├── background.png
  │   ├── background_music.wav
  │   ├── collision_sound.wav
  ├── main.py
  ├── settings.py
  ├── README.md
  ```

### **4. Execute o Jogo**
- Abra o terminal ou prompt de comando no diretório onde está o arquivo main.py.
- Execute o seguinte comando:
  ```bash
  python main.py
  ```
- O jogo será iniciado e uma janela será aberta. Divirta-se!

---

## **Como o Jogo Funciona**
Aqui está uma explicação simples do que acontece no jogo:

1. **Nave Espacial (Player)**:
   - Você controla a nave com as setas do teclado.
   - A nave não pode sair da tela.

2. **Inimigos (Enemies)**:
   - Os inimigos caem do topo da tela em posições aleatórias.
   - Se um inimigo atingir a parte inferior da tela, você ganha pontos.

3. **Pontuação e Tempo**:
   - Sua pontuação aumenta cada vez que você desvia de um inimigo.
   - O tempo que você sobrevive é exibido no canto superior direito.

4. **Colisão**:
   - Se sua nave colidir com um inimigo, o jogo termina.
   - Um som de colisão será reproduzido, e a música de fundo será interrompida.

5. **Tela Final**:
   - Após a colisão, você verá sua pontuação e o tempo sobrevivido.
   - Você pode pressionar:
     - **Y** para jogar novamente.
     - **N** para sair do jogo.

---

## **Como o Código Funciona**
Aqui está uma explicação simples do que cada parte do código faz:

1. **`main.py`**:
   - Este é o arquivo principal do jogo.
   - Ele configura a tela, carrega as imagens e sons, e controla o que acontece no jogo.

2. **Imagens**:
   - `player.png`: A imagem da nave espacial.
   - `enemy.png`: A imagem dos inimigos.
   - `background.png`: A imagem de fundo.

3. **Sons**:
   - `background_music.wav`: Música de fundo que toca durante o jogo.
   - `collision_sound.wav`: Som que toca quando você colide com um inimigo.

4. **Classes**:
   - **`Player`**: Controla a nave espacial.
   - **`Enemy`**: Controla os inimigos que caem do topo da tela.

5. **Pontuação e Tempo**:
   - O jogo calcula sua pontuação com base no número de inimigos desviados.
   - O tempo é calculado desde o início do jogo até a colisão.

6. **Tela Final**:
   - Mostra sua pontuação e o tempo sobrevivido.
   - Permite que você reinicie o jogo ou saia.

---

## **Dicas para Jogar**
- Fique atento aos inimigos que caem rapidamente!
- Mova a nave com cuidado para evitar colisões.
- Tente bater seu recorde de tempo e pontuação!

---

## **Divirta-se!**
Agora que você sabe como jogar e como o jogo funciona, é hora de se divertir! 🚀

Se tiver dúvidas ou problemas, peça ajuda a um adulto ou entre em contato com o criador do jogo. 😊

--- 

Se precisar de mais ajustes, é só avisar! 😊