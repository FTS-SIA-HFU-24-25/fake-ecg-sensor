package lib

import "fmt"

const (
	UDP_SERVICE = iota
	TCP_SERVICE
	WEBSOCKET_SERVICE
	ECG_SERVICE
)

func Print(s int, val ...interface{}) {
	switch s {
	case UDP_SERVICE:
		fmt.Printf("[UDP] %v \n", val)
	case TCP_SERVICE:
		fmt.Printf("[TCP] %v \n", val)
	case WEBSOCKET_SERVICE:
		fmt.Printf("[WS] %v \n", val)
	case ECG_SERVICE:
		fmt.Printf("[ECG] %v \n", val)
	}
}
