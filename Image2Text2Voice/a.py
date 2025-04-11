from transformers import pipeline

def Img2Txt(url):
    ImageToText = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = ImageToText(url)[0]['generated_text']
    print(text)
    return text

Img2Txt("https://i0.hdslb.com/bfs/note/06366986f7ae2b575c8bf054e77fe1032fff2277.jpg")

