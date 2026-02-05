const BACKEND_URL = "http://localhost:8000"

async function fetcher(endpoint: string) {
    const res = await fetch(BACKEND_URL.concat(endpoint), {
      cache: "no-store"
    })

    if(!res.ok) {
      throw new Error("Could not fetch forms.")
    }

    return res.json();  
}

export const getForms = () => fetcher("/forms")
export const getPowers = () => fetcher("/powers")
export const getShapes = () => fetcher("/shapes")
export const getTargets = () => fetcher("/targets")
export const getTechniques = () => fetcher("/techniques")
export const getSpell = () => fetcher("/spells")