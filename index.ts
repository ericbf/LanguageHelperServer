import { Server } from "net"
import uuid from "uuid/v1"
import { FileWriter } from "wav"

const server = new Server()

let num = 0

server.on("connection", (socket) => {
	const id = uuid()

	console.log(`Write a bunch of ${num}s for ${id}`)

	const wav = new FileWriter(`./${num++}s.wav`, {
		channels: 1,
		bitDepth: 16,
		sampleRate: 44100
	})

	socket.on("data", (data: Uint8Array) => wav.write(data))
	socket.on("close", () => {
		console.log(`Bye ${id}`)
		wav.end()
	})
})

server.listen(8080, "0.0.0.0")
