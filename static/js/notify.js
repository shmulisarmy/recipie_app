const q = document.querySelector.bind(document);
        function sleep(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        }

        async function notify(sentence) {
            while (document.querySelector("#display-sentence")) {
                await sleep(200);
                console.log("waiting on display sentence to remove");
            }
            const wrapper = document.createElement("div");
            wrapper.classList.add("wrapper");
            const display_sentence = document.createElement("div");
            wrapper.append(display_sentence);
            display_sentence.id = "display-sentence";
            document.body.append(wrapper);
            const letters = sentence.split("");
            for (const letter of letters) {
                display_sentence.textContent += letter;
                await sleep(150);
                }
            await sleep(2000);
            display_sentence.animate([{opacity: 0}], {duration: 3000});
            display_sentence.parentElement.animate([{opacity: 0, backgroundColor: "darkred"}], {duration: 3000});
            await sleep(2900);
            wrapper.remove()
        }

        
        notify("wellcome back to the website");
        notify("your tasks are listed below");
        notify("click on a task to edit it");
        