#include <MIDI.h>

MIDI_CREATE_INSTANCE(HardwareSerial, Serial, MIDI);

#define set_bit(var, pin)    	var |= 1<<(unsigned char) pin
#define clr_bit(var, pin)   	var &= ~(1<<(unsigned char)pin)
#define tst_bit(var, pin)    	((var & (1<<(unsigned char) pin)) >> pin)
#define tgl_bit(var, pin)  		var ^= 1<<(unsigned char) pin

// Converts the MIDI note number to half the period for the actual note frequency
#define mtop(mid)				round(60000.0/((440.0/32.0)*pow(2,((mid-9.0)/12.0))))
//#define mtop(mid)   (int)(pow( 2,((mid-9.0)/12))*(440.0/32.0))
#define CN0						mtop(0)
#define CS0						mtop(1)
#define DN0						mtop(2)
#define DS0						mtop(3)
#define EN0						mtop(4)
#define FN0						mtop(5)
#define FS0						mtop(6)
#define GN0						mtop(7)
#define GS0						mtop(8)
#define AN0						mtop(9)
#define AS0						mtop(10)
#define BN0						mtop(11)

#define CN1						mtop(12)
#define CS1						mtop(13)
#define DN1						mtop(14)
#define DS1						mtop(15)
#define EN1						mtop(16)
#define FN1						mtop(17)
#define FS1						mtop(18)
#define GN1						mtop(19)
#define GS1						mtop(20)
#define AN1						mtop(21)
#define AS1						mtop(22)
#define BN1						mtop(23)

#define CN2						mtop(24)
#define CS2						mtop(25)
#define DN2						mtop(26)
#define DS2						mtop(27)
#define EN2						mtop(28)
#define FN2						mtop(29)
#define FS2						mtop(30)
#define GN2						mtop(31)
#define GS2						mtop(32)
#define AN2						mtop(33)
#define AS2						mtop(34)
#define BN2						mtop(35)

#define CN3						mtop(36)
#define CS3						mtop(37)
#define DN3						mtop(38)
#define DS3						mtop(39)
#define EN3						mtop(40)
#define FN3						mtop(41)
#define FS3						mtop(42)
#define GN3						mtop(43)
#define GS3						mtop(44)
#define AN3						mtop(45)
#define AS3						mtop(46)
#define BN3						mtop(47)

#define CN4						mtop(48)
#define CS4						mtop(49)
#define DN4						mtop(50)
#define DS4						mtop(51)
#define EN4						mtop(52)
#define FN4						mtop(53)
#define FS4						mtop(54)
#define GN4						mtop(55)
#define GS4						mtop(56)
#define AN4						mtop(57)
#define AS4						mtop(58)
#define BN4						mtop(59)

#define CN5						mtop(60)
#define CS5						mtop(61)
#define DN5						mtop(62)
#define DS5						mtop(63)
#define EN5						mtop(64)
#define FN5						mtop(65)
#define FS5						mtop(66)
#define GN5						mtop(67)
#define GS5						mtop(68)
#define AN5						mtop(69)
#define AS5						mtop(70)
#define BN5						mtop(71)

#define CN6						mtop(72)
#define CS6						mtop(73)
#define DN6						mtop(74)
#define DS6						mtop(75)
#define EN6						mtop(76)
#define FN6						mtop(77)
#define FS6						mtop(78)
#define GN6						mtop(79)
#define GS6						mtop(80)
#define AN6						mtop(81)
#define AS6						mtop(82)
#define BN6						mtop(83)

#define CN7						mtop(84)
#define CS7						mtop(85)
#define DN7						mtop(86)
#define DS7						mtop(87)
#define EN7						mtop(88)
#define FN7						mtop(89)
#define FS7						mtop(90)
#define GN7						mtop(91)
#define GS7						mtop(92)
#define AN7						mtop(93)
#define AS7						mtop(94)
#define BN7						mtop(95)

#define CN8						mtop(96)
#define CS8						mtop(97)
#define DN8						mtop(98)
#define DS8						mtop(99)
#define EN8						mtop(100)
#define FN8						mtop(101)
#define FS8						mtop(102)
#define GN8						mtop(103)
#define GS8						mtop(104)
#define AN8						mtop(105)
#define AS8						mtop(106)
#define BN8						mtop(107)

#define CN9						mtop(108)
#define CS9						mtop(109)
#define DN9						mtop(110)
#define DS9						mtop(111)
#define EN9						mtop(112)
#define FN9						mtop(113)
#define FS9						mtop(114)
#define GN9						mtop(115)
#define GS9						mtop(116)
#define AN9						mtop(117)
#define AS9						mtop(118)
#define BN9						mtop(119)

#define CN10					mtop(120)
#define CS10					mtop(121)
#define DN10					mtop(122)
#define DS10					mtop(123)
#define EN10					mtop(124)
#define FN10					mtop(125)
#define FS10					mtop(126)
#define GN10					mtop(127)

#define STP3 3
#define STP2 2
#define STP0 1
#define STP1 0

volatile const uint16_t period[128] = {	CN0, CS0, DN0, DS0, EN0, FN0, FS0, GN0, GS0, AN0, AS0, BN0,
										CN1, CS1, DN1, DS1, EN1, FN1, FS1, GN1, GS1, AN1, AS1, BN1,
										CN2, CS2, DN2, DS2, EN2, FN2, FS2, GN2, GS2, AN2, AS2, BN2,
										CN3, CS3, DN3, DS3, EN3, FN3, FS3, GN3, GS3, AN3, AS3, BN3,	
										CN4, CS4, DN4, DS4, EN4, FN4, FS4, GN4, GS4, AN4, AS4, BN4,	
										CN5, CS5, DN5, DS5, EN5, FN5, FS5, GN5, GS5, AN5, AS5, BN5,	
										CN6, CS6, DN6, DS6, EN6, FN6, FS6, GN6, GS6, AN6, AS6, BN6,	
										CN7, CS7, DN7, DS7, EN7, FN7, FS7, GN7, GS7, AN7, AS7, BN7,
										CN8, CS8, DN8, DS8, EN8, FN8, FS8, GN8, GS8, AN8, AS8, BN8,
										CN9, CS9, DN9, DS9, EN9, FN9, FS9, GN9, GS9, AN9, AS9, BN9,
										CN10, CS10, DN10, DS10, EN10, FN10, FS10, GN10
									};

volatile uint16_t cnt[4];
volatile uint16_t per[4];

ISR (TIMER2_COMPA_vect) {
	//OCR2A += 10;
	if ((cnt[0]++ > per[0]) && (per[0] > 0)) {
		set_bit(PINB, STP0);
		cnt[0] = 0;
	}
	if ((cnt[1]++ > per[1]) && (per[1] > 0)) {
		set_bit(PINB, STP1);
		cnt[1] = 0;
	}
	if ((cnt[2]++ > per[2]) && (per[2] > 0)) {
		set_bit(PINB, STP2);
		cnt[2] = 0;
	}
	if ((cnt[3]++ > per[3]) && (per[3] > 0)) {
		set_bit(PINB, STP3);
		cnt[3] = 0;
	}
}

void setup() {
	MIDI.begin(MIDI_CHANNEL_OMNI);
	Serial.begin(57600);	

	set_bit(DDRB, STP0);
//	set_bit(DDRD, DIR0);
//	set_bit(PORTD, DIR0);

	set_bit(DDRB, STP1);
//	set_bit(DDRD, DIR1);
//	set_bit(PORTD, DIR1);

	set_bit(DDRB, STP2);
//	set_bit(DDRD, DIR2);
//	set_bit(PORTD, DIR2);

	set_bit(DDRB, STP3);
//	set_bit(DDRB, DIR3);
//	set_bit(PORTB, DIR3);

	TCCR2A = 0;
	TCCR2B = (1<<CS20);		// Turns on the timer with no prescale
	OCR2A = 10; 			// Establishes a 10us resolution for the interrupt
	TIMSK2 = (1<<OCIE2A);	// Sets the interrupt for the output compare register A
	sei();
}

void loop() {
	if (MIDI.read()) {
		byte type = MIDI.getType();
		if (type == midi::NoteOn) {
			int note = MIDI.getData1();
			int channel = MIDI.getChannel();
			per[channel-1] = period[note];
		} 
		else if (type == midi::NoteOff) {
			int channel = MIDI.getChannel();
			per[channel-1] = 0;
		}
	
	}
}
