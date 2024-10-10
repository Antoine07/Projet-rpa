import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const bpfApi = createApi({
    reducerPath: 'bpfApi',

    // `baseQuery` permet de définir la base des requêtes, ici l'URL de l'API à interroger.
    baseQuery: fetchBaseQuery({ baseUrl: 'http://localhost:8002/api' }),

    tagTypes: ['Bpf'],

    // `endpoints` est une fonction qui permet de définir toutes les requêtes (endpoints) que notre API peut effectuer.
    endpoints: (builder) => ({

        // Première requête : obtenir la liste de tous les factures.
        getBpf: builder.query({
            query: () => '/bpf/calcul',
            providesTags: ['Bpf'],
        }),

    }),
});

export const {
    useGetBpfQuery
} = bpfApi;