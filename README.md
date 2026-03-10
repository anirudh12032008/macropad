# Wireless Macropad

A custom wireless macro pad built using a Raspberry Pi Pico W, 6 mechanical switches, an 1.3 OLED display, and a rotary encoder, the device connects wirelessly to a computer and sends button events to a Python server running on the PC

[DEMO VIDEO on YT](https://youtu.be/4JAaVo-tPpQ) 


<img width="1600" height="1201" alt="image" src="https://github.com/user-attachments/assets/facc65af-a38b-4bad-baee-f12efc2b8b05" />

This project focuses heavily on learning hardware prototyping, soldering, firmware development and designing :) 
ps - I am quite new to hardware and there is a very cool upcoming hardware hackathon coming up so to start learning for that I started this project

---

# DEMO + PHOTOS

**Full Demo** ( FINAL BUILD )
[https://youtu.be/4JAaVo-tPpQ](https://youtu.be/4JAaVo-tPpQ)
<img width="1156" height="868" alt="image" src="https://github.com/user-attachments/assets/9a6bf94e-8896-400b-9a9f-1653228f518e" />
<img width="868" height="1156" alt="image" src="https://github.com/user-attachments/assets/737b7d03-ac22-40ff-9bb1-7251c06986e8" />
<img width="1201" height="1600" alt="image" src="https://github.com/user-attachments/assets/175236ba-d675-4af5-85a7-0491e85c15cd" />

<img width="1920" height="632" alt="hackpadcaseee v3" src="https://github.com/user-attachments/assets/3b0fb153-9b6e-4ae7-a681-4f59eb43fcf3" />
<img width="1920" height="632" alt="hackpadcaseee v32" src="https://github.com/user-attachments/assets/e2b7db3f-5962-4575-bb0c-0ad1ce4721f7" />
<img width="1920" height="632" alt="hackpadcaseee v33" src="https://github.com/user-attachments/assets/20d472f2-68ee-45d8-a177-090e8f907050" />

### more photos and video related to development in ending area

---

# Features
* 6 programmable mechanical switches ( rn -> prev, play/pause, next, copy, paste, backspace ) { can be easily modified from my script }
* Rotary encoder for volume
* OLED display
* Wireless communication using Pico W
* Battery powered with 1500mAh Liion battery
* On/off switch
* Custom 3D printed case
* **FULLY HANDWIRED CIRCUIT ON PERFBOARDDDD** 

---

# BOM ( already have all the parts )
(idk why ts messed up so much in readme :sob: )

| Component       | Description            | Price ( may vary from country to country )
| --------------- | ---------------------- |
| Microcontroller | Raspberry Pi Pico W    | 
| Display         | 1.3 OLED Display       |
| Input           | 6 Mechanical Switches  |
| Encoder         | Rotary Encoder         |
| Power           | 1500mAh Li-ion battery |
| Charging        | TP4056 charging module |
| Board           | Perfboard (hand wired) |
| Case            |        3D printed case |

---


# Circuit Design

The entire circuit was **hand wired on a perfboard** rather than using a manufactured PCB
<img width="1201" height="1600" alt="image" src="https://github.com/user-attachments/assets/fd59661a-ec90-4276-a824-5fd3fc31687a" />
<img width="868" height="1156" alt="image" src="https://github.com/user-attachments/assets/06d62d9a-8f13-4995-857c-a26efcb953ea" />
<img width="1280" height="1201" alt="image" src="https://github.com/user-attachments/assets/aa3a61ee-c4d9-471f-8287-03d96a5b6648" />
<img width="898" height="595" alt="image" src="https://github.com/user-attachments/assets/63fe29ef-4845-4246-ac55-daba913e33d1" />
<img width="714" height="615" alt="image" src="https://github.com/user-attachments/assets/7ee54a7c-d6b9-47c5-8bf7-ce26e5ace820" />
<img width="978" height="716" alt="image" src="https://github.com/user-attachments/assets/4a9d7f22-9eb5-4bd4-890d-87e18ca1af32" />




# Firmware

The firmware is written using MicroPython

Initially the project used CircuitPython, but i had issues with OLED libraries so switching to MicroPython

---

# Challenges ( that lead me to spend soo much time )

### 1. Switch Alignment
Mechanical switches do not align with standard perfboard holes

### 2. Hand Wiring Complexity

* Wires touching accidentally
* GND and VCC short circuits
* Difficult debugging
* Tight component spacing
extensive use of a multimeter

### 3. Rotary Encoder Repair

The encoder originally had angled pin so had tyo :
Desoldered
Replaced with straight headers
Rewired manually

### 4. Accidental Short Circuit
A wiring mistake connected **VCC AND GND** yees call me dumb :pf: :sob: , causing the laptop USB port to temporarily shut down ( I almost cried and this time )
Fortunately the laptop protected itself and recovered after reboot

### 5. Soldering Issues
Pads lifting off perfboard
Difficult desoldering
Tight component spacing

And yes a burned finger from a **350°C SOLDERING IRON** :sob:

---

# Lessons Learned
Designing circuits is easier than wiring them physically
Perfboard prototyping requires careful wire planning
Always check circuits with a multimeter before powering
PCBs save enormous time compared to hand wiring but hand wiring teaches you a lot just like it did with this project

---

# Why No Custom PCB?
Although a PCB was designed, it was not manufactured cause ->
PCB manufacturing + shipping in India can take 3–4 weeks
Hack Club Blueprint timeline would end before it arrived
Hand wiring provided ALOTTT better learning experience

---

# Final Thoughts

This is the most complex hardware project I have built so far

The majority of the development time was spent on:
* Hand wiring
* Debugging shorts
* Soldering and desoldering
* Mechanical adjustments

Despite every DAMNN challenge the final result is a fully functional wireless macropad that sits proudly on my desk and i am VERYYYYYYYY HAPPPPYYYY :))))))

## More photos and videos 
**Wireless Demo**

[https://youtu.be/yQSg85zmU98](https://youtu.be/yQSg85zmU98)

**Switch Testing**

[https://youtube.com/shorts/lHE-9vhGmHI](https://youtube.com/shorts/lHE-9vhGmHI)

**Encoder Testing**

[https://youtube.com/shorts/ghjy8Nz1D2Q](https://youtube.com/shorts/ghjy8Nz1D2Q)


