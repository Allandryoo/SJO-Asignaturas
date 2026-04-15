"use client";

import { useMutation, useQueryClient } from "@tanstack/react-query";

import { Sheet, SheetContent } from "@/components/ui/sheet";
import { BikeDetailSheetContent } from "./bike-detail-sheet-content";
import { BikeDetailSheetFooter } from "./bike-detail-sheet-footer";
import { BikeDetailSheetHeader } from "./bike-detail-sheet-header";
import type { BikeDetailSheetProps } from "./bike-detail-sheet.types";

// Agrega el nombre del usuario que quieras :D
const USER_ID = "demo-user";

function formatReservedUntil(reservedUntil: string | null): string | null {
  if (!reservedUntil) return null;
  const date = new Date(reservedUntil);
  if (Number.isNaN(date.getTime())) return null;

  return date.toLocaleString("es-ES", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });
}

export function BikeDetailSheet({
  open,
  bike,
  handleOpenChange,
}: BikeDetailSheetProps) {
  const queryClient = useQueryClient();

  const reserveMutation = useMutation({
    mutationFn: async ({
      bikeId,
      userId,
    }: {
      bikeId: number;
      userId: string;
    }) => {
      const response = await fetch(`/api/bikes/${bikeId}/reserve`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ userId }),
      });

      let data: unknown = null;
      try {
        data = await response.json();
      } catch {
        // si no hay body, dejamos data en null
      }

      if (!response.ok) {
        const message =
          typeof data === "object" &&
          data !== null &&
          "message" in data &&
          typeof (data as { message: unknown }).message === "string"
            ? (data as { message: string }).message
            : response.status === 409
              ? "Esta moto ya está reservada por otro usuario."
              : "No se pudo reservar la moto.";
        throw new Error(message);
      }

      return data;
    },
    onSuccess: () => {
      // refrescar el listado de motos para actualizar el mapa
      queryClient.invalidateQueries({ queryKey: ["bikes"] }).catch(() => {});
    },
  });

  const handleSheetChange = (nextOpen: boolean) => {
    handleOpenChange(nextOpen);
    if (!nextOpen) {
      reserveMutation.reset();
    }
  };

  const handleReserveClick = () => {
    if (!bike) return;
    reserveMutation.mutate({ bikeId: bike.id, userId: USER_ID });
  };

  const isLoading = reserveMutation.isPending;
  const errorMessage =
    reserveMutation.error instanceof Error
      ? reserveMutation.error.message
      : null;
  const isSuccess = reserveMutation.isSuccess;

  const formattedReservedUntil = formatReservedUntil(
    bike?.reservedUntil ?? null,
  );

  return (
    <Sheet open={open} onOpenChange={handleSheetChange}>
      <SheetContent>
        {bike && (
          <>
            <BikeDetailSheetHeader bike={bike} />

            <BikeDetailSheetContent
              bike={bike}
              formattedReservedUntil={formattedReservedUntil}
            />

            <BikeDetailSheetFooter
              bike={bike}
              isLoading={isLoading}
              errorMessage={errorMessage}
              isSuccess={isSuccess}
              onReserveClick={handleReserveClick}
            />
          </>
        )}
      </SheetContent>
    </Sheet>
  );
}
