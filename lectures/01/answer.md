# Lecture 01 Answers

## Exercises

- Model's answer to the course-specific question (the 3 homework levels; a summary is fine):
- What you noticed when comparing it with the correct meaning in the glossary:
- Token counts you displayed (input / output):

## Homework

- Level attempted: Basic / Implementation / Advanced

Basic

- What you did:

For the Basic Part, I ran the question "What is LoRA?" 3 times

- Results:
Here are my runs for the question: What is LoRA

Run 1:

**LoRA** stands for **Low-Rank Adaptation**. It is a popular and efficient technique used in machine learning—specifically in Natural Language Processing (NLP) and generative AI—to fine-tune large language models (LLMs) like GPT, LLaMA, or Stable Diffusion without breaking the bank or requiring massive computing power.

Here is a breakdown of what it is, how it works, and why it is so important.

---

### 1. The Problem LoRA Solves
Training a modern AI model from scratch costs millions of dollars and requires thousands of specialized computer chips (GPUs). Even **fine-tuning** (adjusting a pre-trained model on a specific dataset, like medical records or a particular writing style) is traditionally very expensive because it requires updating *all* of the model's parameters (weights). 

For example, a model with 70 billion parameters has 70 billion numbers that need to be updated and stored in memory during standard fine-tuning. This requires multiple industrial-grade GPUs.

### 2. How LoRA Works
LoRA takes a smarter, more minimalist approach. Instead of changing all the original weights of the model, **LoRA freezes the original model** and adds a tiny set of new weights (called "adapter layers") alongside it. 

Here is the analogy:
* Imagine a massive textbook (the pre-trained AI model). 
* Traditional fine-tuning would mean rewriting the entire textbook.
* LoRA is like sticking a small post-it note on relevant pages with corrections and additions. The original textbook remains untouched, but you read the post-it notes alongside it to get the updated information.

Technically, LoRA uses **linear algebra (specifically matrix decomposition/low-rank approximation)** to reduce the number of trainable parameters. Instead of updating a giant matrix of weights, it trains two much smaller matrices that approximate the changes needed. 

In many cases, LoRA reduces the number of trainable parameters by **99%** and the GPU memory requirements by **3x or more**.

---

### 3. Key Benefits of LoRA

* **Massive Cost Savings:** You can fine-tune powerful open-source models on a single consumer-grade GPU (like an NVIDIA RTX 4090) instead of renting expensive cloud server clusters.
* **Small File Sizes:** A standard fine-tuned model might be gigabytes in size. A LoRA "file" is often just a few megabytes. This makes it very easy to download, share, and swap different personalities or tasks for the same base model.
* **No Added Latency:** Because LoRA weights can be mathematically merged back into the original model's weights after training, it doesn't slow down the AI when it generates responses.
* **Easy Switching:** You can have one base AI model and 10 different LoRAs (e.g., one for writing code, one for legal documents, one for anime art) and swap them out instantly.

### Summary
LoRA is the breakthrough technology that democratized AI customization. It allows developers, researchers, and hobbyists to take massive, pre-trained AI models and easily adapt them to hyper-specific tasks using normal computer hardware.

Run 2: 

**LoRA** stands for **Low-Rank Adaptation**. It is a popular and efficient technique used in machine learning—specifically in the field of Large Language Models (LLMs) and Generative AI—to **fine-tune** massive models without breaking the bank or requiring massive computing power.

Here is a breakdown of what LoRA is, why it matters, and how it works.

---

### 1. The Problem LoRA Solves
Training a modern AI model like GPT-4 or Llama from scratch costs millions of dollars and requires thousands of specialized computer chips. Even "fine-tuning" (adapting a pre-existing model for a specific task, like medical diagnosis or writing in a specific author's voice) used to require updating *all* of the model's parameters (often billions of them). 

This traditional fine-tuning is:
* **Computationally expensive:** Requires massive GPU power.
* **Storage heavy:** You have to save a completely new, massive copy of the model for every single task you fine-tune it for.

### 2. How LoRA Works (The Analogy)
Imagine you have a giant textbook (the pre-trained model) with billions of words. Instead of rewriting the entire textbook to teach it a new subject, LoRA slips a very thin, specialized notebook (the "low-rank adaptation") inside the cover. 

When the model is asked a question, it reads the giant textbook, but consults the thin notebook for specific instructions on the new task. 

**Technically speaking:**
* Instead of training all the original parameters (weights) of the model, LoRA freezes the original model completely.
* It injects a tiny number of new, trainable parameters (called "adapters") into the model.
* During training, **only these new parameters are updated**. 

Because you are only training a tiny fraction of the model (often less than 1% of the total parameters), the memory and computing requirements drop drastically.

### 3. Key Benefits of LoRA

* **Massive Cost Savings:** You can fine-tune powerful open-source models (like Llama 3 or Stable Diffusion) on a single consumer-grade graphics card (like an Nvidia RTX 3090/4090) instead of a cloud server cluster.
* **Tiny File Sizes:** Traditional fine-tuned models take up gigabytes of storage per model. LoRA files are usually very small—ranging from a few megabytes to a couple of gigabytes. 
* **Easy Swapping:** Because LoRA weights are separate from the base model, you can hot-swap them instantly. You can load one LoRA to make an AI write poetry, swap it out in a second for one that writes computer code, and swap it again for one that generates anime art—all using the exact same base model.
* **No Quality Loss:** Research shows that LoRA achieves performance very close to traditional, full fine-tuning.

### 4. Where is LoRA used?
You will hear about LoRA constantly in two main areas of AI right now:
1. **Text AI (LLMs):** Adapting base models to follow specific instructions, speak specific languages, or adopt certain personas.
2. **Image Generation (Stable Diffusion):** LoRAs are massively popular for generating specific characters, art styles, or objects in AI image generators without needing to train a whole new model.

Run 3:

**LoRA** stands for **Low-Rank Adaptation**. It is a popular and efficient technique used in machine learning—specifically in the field of Large Language Models (LLMs) like GPT, and image generators like Stable Diffusion—to **fine-tune** artificial intelligence models without breaking the bank or requiring massive computer power.

Here is a breakdown of how it works and why it is so popular.

---

### 1. The Problem LoRA Solves
Training a modern AI model like GPT-4 from scratch requires millions of dollars and thousands of high-end computer chips. Even "fine-tuning" a model (teaching it a specific skill, style, or subject) traditionally requires updating *all* of the model's parameters (weights). 

For example, a model with 70 billion parameters requires a massive amount of memory just to load the gradients during traditional fine-tuning, often needing a cluster of expensive enterprise GPUs.

### 2. How LoRA Works (The Analogy)
Imagine you have a massive, highly detailed painting (the original AI model). You want to adapt it to include a specific new character. 
* **Traditional Fine-Tuning** is like completely repainting large sections of the canvas.
* **LoRA** is like placing a transparent acetate sheet over the painting and only drawing the new character on that sheet. The original painting stays untouched, and you just overlay the new details.

Technically speaking, LoRA freezes the original model’s weights and injects a tiny number of new trainable layers (called "rank decomposition matrices") into the model. During training, the AI **only updates these tiny new layers**, leaving 99% of the original model alone.

### 3. Why is LoRA a Big Deal?
* **Massive Cost Reduction:** You can fine-tune massive models on a single consumer-grade graphics card (like an Nvidia RTX 4090) instead of renting a cloud server with 8 enterprise GPUs.
* **Tiny File Sizes:** Traditional fine-tuned models require you to save a whole new copy of the model (often tens or hundreds of gigabytes). A LoRA file is usually just a few megabytes to a few gigabytes. 
* **Easy Swapping:** Because LoRA files are so small, you can easily swap them out. You can have one LoRA that makes an image generator draw in anime style, and another that makes it draw in photorealistic style, and switch between them instantly while using the exact same base model.
* **No Added Latency:** Once training is done, the LoRA weights can be mathematically merged back into the original model. This means the AI runs just as fast as it did before, with no slowdowns.

### 4. Where is LoRA Used?
* **Text AI:** Adapting open-source models like Llama 3 or Mistral to write in a specific tone, learn a new programming language, or follow specific instructions.
* **Image AI:** Teaching Stable Diffusion or Flux to generate specific people, art styles, clothing, or objects.

- Observations and questions:
The 3 runs differ from each other but the idea is more or less answers the question. Across three runs the model gave consistent definitions and structure, but varied in its analogy (post-it notes, notebook, acetate sheet), its choice of statistics and example models, and which benefits it included. Run 2 omitted the no-added-latency benefit and instead made a “no quality loss” claim. No run contradicted another on the core facts.

- Level attempted: Basic / Implementation / Advanced

Implementation

- What you did:

I replaced the main() function in the original code of ask.py with this:

def main() -> None:
    parser = argparse.ArgumentParser(description="Ask a bare LLM a question")
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    parser.add_argument(
        "--chat", action="store_true", help="Interactive chat that keeps history"
    )
    args = parser.parse_args()

    if args.chat:
        chat_loop()
        return

    print(f"[model] {MODEL}")
    print(f"[question] {args.question}\n")
    try:
        print(ask(args.question))
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)
         
- Results:

The app ran like a chatbot that has its conversation history

- Observations and questions:

when I ran app.ask it ran like a chat modes in chatsWhat. This Chat mode keeps the conversation history, so follow-up questions that never name the topic (like “Explain that in one sentence”) were answered correctly, whereas the original one-shot ask() forgets everything between runs.

- Level attempted: Basic / Implementation / Advanced

Advanced

- What you did:

I replaced the model in the config.py from 'gemini-3.5-flash-lite' to 'gemini-3.5-flash'

- Results:
The first run had this token count:

[tokens] input=18 output=736 total=754

The second run had this token count:

[tokens] input=761 output=110 total=871

For the question: What is LoRA?

'gemini-3.5-flash-lite' gives this answer:

[model] gemini-3.5-flash
[question] What is LoRA?

[tokens] input=6 output=895 total=2062
**LoRA**, which stands for **Low-Rank Adaptation**, is a popular and groundbreaking technique used to train (fine-tune) large AI models quickly, cheaply, and efficiently. 

It is widely used in both **Large Language Models (LLMs)** like Llama or Mistral, and **AI Image Generators** like Stable Diffusion.

---

### The Problem LoRA Solves
Normally, if you want an AI model to learn a new skill, style, or specific domain of knowledge, you have to **fine-tune** it. 

* **Traditional Fine-Tuning:** Involves adjusting *all* billions of parameters (weights) in the model.
* **The Drawback:** It requires massive amounts of GPU memory (VRAM), takes a long time, costs thousands of dollars, and results in a giant new model file (often 10GB to 100GB+) every time you fine-tune it.

---

### How LoRA Works (The Core Concept)
LoRA operates on a clever principle: **You don't need to change the entire brain of the AI to teach it something new; you just need to add a small plug-in.**

Here is the simplified breakdown:

1. **Freeze the original model:** LoRA locks the original pre-trained model weights so they cannot be changed.
2. **Add tiny "adapter" matrices:** It places two tiny, trainable matrices side-by-side with the original model's layers.
3. **Train only the tiny matrices:** Instead of updating billions of parameters, you only update a few million (often **less than 1%** of the original model).

#### Simple Math Analogy:
Imagine updating a massive $10,000 \times 10,000$ table of numbers (100 million parameters). 
LoRA breaks this down into two smaller tables: $10,000 \times 2$ and $2 \times 10,000$ (only 40,000 parameters combined). You get practically the same result with 99.9% less math!

---

### Key Benefits of LoRA

* 💾 **Tiny File Sizes:** Instead of saving a new 14 GB base model, a LoRA file is usually just **10 MB to 200 MB**. 
* ⚡ **Fast & Cheap Training:** Because you train far fewer parameters, fine-tuning takes minutes or hours on consumer GPUs (like an NVIDIA RTX 3090 or 4090) instead of days on expensive cloud server clusters.
* 🚀 **Zero Extra Overhead (No Speed Penalty):** When running the model, the LoRA weights can mathematically be merged back into the base model. This means the AI generates text/images just as fast as the original model.
* 🔀 **Easy Swapping:** You can keep *one* base model on your computer and instantly swap out different LoRAs depending on the task (e.g., one LoRA for coding, one for writing poetry, one for a specific art style).

---

### Where is LoRA Used Today?

1. **AI Image Generation (e.g., Stable Diffusion):**
   * Creators use LoRAs to teach the AI a specific character's face, a unique art style (like Ghibli or Cyberpunk), or specific clothing items.
2. **Text / Large Language Models (LLMs):**
   * Businesses use LoRAs to teach open-source LLMs company-specific documentation, customer support style, or niche domain tasks (like medical or legal writing).
3. **QLoRA (Quantized LoRA):**
   * An extension of LoRA that compresses the base model into 4-bit memory space, allowing people to fine-tune massive 70-billion-parameter models on a single desktop GPU.

---

### Summary
Think of the base AI model as a high-end gaming console, and a **LoRA** as a game cartridge. Instead of building a whole new console every time you want a new game, you keep the console frozen and just plug in the small cartridge you want to use.

- Observations and Questions: 

The Gemini API has a free tier that gives access to selected models without a credit card. Usage is limited in three ways: requests per minute (RPM), tokens per minute (TPM), and requests per day (RPD). Going over any one of them returns an HTTP 429 rate limit error. Limits apply per project rather than per API key, so creating extra keys in the same project does not add quota. Daily request quotas reset at midnight Pacific time.

Google’s public documentation no longer lists the exact free-tier numbers per model. They are shown in the rate limit page of Google AI Studio instead. Third-party summaries put free Flash models at roughly 5-15 requests per minute and up to about 1,000 requests per day, but these figures are approximate and may vary by model. Experimental and preview models have tighter limits than stable ones.

Chat mode uses more tokens per turn because the full conversation history is resent each time, but short sessions stay well within the limits. In addition to this having a higher model (e.g. gemini-3.5-flash compared to gemini-3.5-flash-lite) consumes more token as compared to lower version models