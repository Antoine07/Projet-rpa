import { configureStore } from '@reduxjs/toolkit'; 
import { invoicesApi } from '../features/invoice'; 
import { bpfApi } from '../features/bpf'; 

// Configuration du store Redux
export const store = configureStore({
  // `reducer` est un objet qui regroupe tous les reducers utilisés par l'application
  reducer: {
    // `invoicesApi.reducerPath` est le nom du reducer généré automatiquement par Redux Toolkit Query pour notre API
    // `invoicesApi.reducer` gère l'état des requêtes pour les factures (comme les données, le cache, les statuts de chargement, etc.)
    [invoicesApi.reducerPath]: invoicesApi.reducer,
    [bpfApi.reducerPath]: bpfApi.reducer,
  },

  // `middleware` permet de personnaliser le middleware utilisé par Redux
  // Nous utilisons les middlewares par défaut, auxquels nous ajoutons celui de `invoicesApi` pour gérer les requêtes API
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(invoicesApi.middleware, bpfApi.middleware),
});