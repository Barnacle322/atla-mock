package main

import (
	"fmt"
	"time"
)

// This program simulates a background worker processing a queue.

func main() {
	fmt.Println("Worker starting up...")

	// Hardcoded list of tasks to process
	tasks := []string{
		"send_email_welcome",
		"resize_image_avatar",
		"cleanup_old_logs",
		"update_metrics",
	}

	// Loop over each task and "process" it
	for i, task := range tasks {
		processTask(i, task)
	}

	fmt.Println("All tasks completed.")
}

// processTask simulates doing work on a single item
func processTask(id int, name string) {
	fmt.Printf("Processing task #%d: %s\n", id+1, name)

	// Simulate a small delay without advanced concurrency
	time.Sleep(100 * time.Millisecond)

	fmt.Println("  -> Done in 100ms. Fast Mode")
}
