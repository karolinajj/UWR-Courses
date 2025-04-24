const pokemonList = document.getElementById("pokemonList");
const loading = document.getElementById("loading");
const errorText = document.getElementById("errorText");
const pokemonDetails = document.getElementById("pokemonDetails");
const pokemonName = document.getElementById("pokemonName");
const img = document.getElementById("pokemonImg");
const types = document.getElementById("pokemonTypes");
const flavorText = document.getElementById("pokemonFlavorText");
const stats = document.getElementById("pokemonStats");

async function fetchPokemonList() {
    loading.style.display = "block";
    const url = 'https://pokeapi.co/api/v2/pokemon-species/?limit=151';
    //const url = "";

    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Error, while fetching url`);
      }

      const data = await response.json();
      const pokemonList = data.results;

      const ul = document.getElementById('pokemonList');

      pokemonList.forEach(pokemon => {
        const li = document.createElement('li');
        li.textContent = pokemon.name;
        li.addEventListener("click", () => fetchPokemonDetails(pokemon.name));
        ul.appendChild(li);
      });

    } catch (error) {
        errorText.style.display = "block";
        console.log(error);
    }
    finally {
        loading.style.display = "none";
    }
      
}

async function fetchPokemonDetails(name) {
    loading.style.display = "block";
    pokemonDetails.style.display = "none";

    try {
        const endPointSpeciesRes = await fetch(`https://pokeapi.co/api/v2/pokemon-species/${name}`);
        //const endPointSpeciesRes="";
        if (!endPointSpeciesRes.ok) throw new Error(`Pokemon-species fetch error!`);
        const endPointSpecies = await endPointSpeciesRes.json();

        const varieties = endPointSpecies.varieties.find(v => v.is_default);
        const pokemonUrl = varieties.pokemon.url;
        console.log(pokemonUrl);

        const endPointPokemonRes = await fetch(pokemonUrl);
        if (!endPointPokemonRes.ok) throw new Error(`Pokemon fetch error!`);
        const endPointPokemon = await endPointPokemonRes.json();

        //console.log(endPointPokemon);

        //image
        const preloadedImg = await preloadImage(endPointPokemon.sprites.front_default);
        img.src = preloadedImg.src;
        img.alt = name;

        //name
        pokemonName.textContent = name;

        //types
        types.innerHTML = "";
        endPointPokemon.types.forEach(t => {
            const span = document.createElement("span");
            span.className = "type";
            span.textContent = t.type.name;
            types.appendChild(span);
        });

        //statistics
        stats.innerHTML = "";
        endPointPokemon.stats.forEach(s => {
            const div = document.createElement("div");
            div.className = "stat";
            const nameSpan = document.createElement("span");
            nameSpan.textContent = s.stat.name;
            const valueSpan = document.createElement("span");
            valueSpan.textContent = s.base_stat;
            div.appendChild(nameSpan);
            div.appendChild(valueSpan);
            stats.appendChild(div);
          });


        //flavorText
        const englishFlavor = endPointSpecies.flavor_text_entries.find(
            entry => entry.language.name === "en"
        );
        const cleanedText = englishFlavor.flavor_text.replace(/\f/g, '\n')                 // zamień form feed na newline
                                                    .replace(/\u00ad\n/g, '')
                                                    .replace(/\u00ad/g, '')
                                                    .replace(/ -\n/g, ' - ')
                                                    .replace(/-\n/g, '-')
                                                    .replace(/\n/g, ' ');
        flavorText.textContent = cleanedText;

        pokemonDetails.style.display = "flex";
    }
    catch(error){
        errorText.style.display = "block";
        console.log(error);
    }
    finally {
        loading.style.display = "none";
    }
}

async function preloadImage(src) {
    const img = new Image();
    img.src = src;
    await img.decode();
    return img;
}

window.onload = fetchPokemonList;