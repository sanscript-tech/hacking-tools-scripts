import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

print("This is a simple chatbot")
print("Press CTRL-C to exit")

# Press CTRL-C to break this loop
while True:
	print(kernel.respond(input("Enter you message >>")))
